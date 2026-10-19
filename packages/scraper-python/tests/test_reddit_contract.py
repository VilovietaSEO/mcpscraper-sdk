import pytest
from pydantic import TypeAdapter, ValidationError

from mcpscraper.mcp_models.reddit_trending import (
    RedditTrendingInput,
    RedditTrendingOutputVariant1RankedThreadsItem,
)


def test_past_year_request_keeps_per_thread_limit_and_retry_identity():
    request = RedditTrendingInput.model_validate({
        "topic": "how to pick a good roofer", "window": "year",
        "maxThreads": 2, "maxCommentsPerThread": 20,
        "idempotencyKey": "same-roofer-request",
    })
    wire = request.model_dump(by_alias=True, exclude_none=True)
    assert wire["window"] == "year"
    assert wire["maxCommentsPerThread"] == 20
    assert wire["idempotencyKey"] == "same-roofer-request"
    with pytest.raises(ValidationError):
        RedditTrendingInput.model_validate({"topic": "roofer", "window": "day"})


def test_partial_comment_coverage_is_typed_and_old_rows_remain_valid():
    row = {
        "title": "Choosing a roofer", "url": "https://www.reddit.com/r/example/comments/abc/post/",
        "subreddit": "example", "score": 1, "commentCount": 25,
        "engagementScore": 51, "ageText": "recent", "topQuestions": [],
    }
    adapter = TypeAdapter(RedditTrendingOutputVariant1RankedThreadsItem)
    assert "commentCoverage" not in adapter.validate_python(row)
    row.update(publishedAt=None, capturedCommentCount=19, requestedCommentLimit=20,
               commentCoverage={"requestedLimit": 20, "returnedCount": 19,
                                "declaredCount": 25, "status": "partial",
                                "reason": "stable_visible_shortfall"})
    value = adapter.validate_python(row)
    assert value["commentCoverage"]["returnedCount"] == 19
    assert value["commentCoverage"]["status"] == "partial"
    row["commentCoverage"]["reason"] = "assume_complete"
    with pytest.raises(ValidationError):
        adapter.validate_python(row)


def test_rest_models_accept_year_and_preserve_nullable_publication_date():
    from mcpscraper.models import RedditTrendingRequest, RedditThreadResponse

    request = RedditTrendingRequest.model_validate({"topic": "roofer", "window": "year"})
    assert request.window.value == "year"
    assert RedditThreadResponse.model_validate({"publishedAt": None}).publishedAt is None
    with pytest.raises(ValidationError):
        RedditTrendingRequest.model_validate({"topic": "roofer", "window": "day"})
