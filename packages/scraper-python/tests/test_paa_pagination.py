import pytest
from pydantic import ValidationError
from mcpscraper.mcp_models.harvest_paa import HarvestPaaInput, Pagination
from mcpscraper.mcp_models.harvest_paa_start import HarvestPaaStartInput
from mcpscraper.mcp_models.harvest_paa_status import Pagination as StatusPagination


@pytest.mark.parametrize("model", [HarvestPaaInput, HarvestPaaStartInput])
def test_pages_defaults_and_bounds(model):
    args = {"query": "commercial truck insurance", "idempotencyKey": "two-pages-example"}
    assert model(**args).pages == 1
    assert model(**args, pages=2).model_dump(by_alias=True)["pages"] == 2
    for pages in (0, 3):
        with pytest.raises(ValidationError):
            model(**args, pages=pages)


@pytest.mark.parametrize("model", [Pagination, StatusPagination])
def test_capture_diagnostics_are_typed(model):
    payload = {"requestedPages": 2, "capturedPages": 1, "page2Status": "failed", "page1OrganicCount": 9, "page2OrganicCount": 0, "failureCode": "timeout"}
    result = model.model_validate(payload)
    assert result.model_dump(by_alias=True) == payload
    with pytest.raises(ValidationError):
        model.model_validate({**payload, "page2Status": "assumed_success"})
    with pytest.raises(ValidationError):
        model.model_validate({**payload, "page2OrganicCount": -1})
