export interface Input {
  /**
   * Complete editorial site payload containing the collection identity and authored articles.
   */
  site: {
    /**
     * Stable kebab-case identifier used for browser reading progress, for example "customer-research-field-notes".
     */
    slug: string;
    /**
     * Publication title shown in the page title and footer.
     */
    title: string;
    /**
     * Short product, organization, or collection name shown in the masthead.
     */
    product: string;
    /**
     * Short editorial edition name shown in the masthead.
     */
    edition?: string;
    /**
     * Small label in the home-page issue line.
     */
    editionLabel?: string;
    /**
     * Issue, date, or collection label in the home-page issue line.
     */
    issueLabel?: string;
    /**
     * Short editorial eyebrow above the home-page headline.
     */
    eyebrow?: string;
    /**
     * Outcome-led home-page headline for the whole reading room.
     */
    heroTitle: string;
    /**
     * Label for the primary start-reading button.
     */
    startLabel?: string;
    /**
     * Optional collection-level Open Graph image. Individual articles may override it.
     */
    ogImage?: {
      /**
       * Public HTTP(S) image URL used for the reading-room home page social preview.
       */
      url: string;
      /**
       * Accessible description and og:image:alt text.
       */
      alt: string;
      /**
       * Optional intrinsic width in pixels.
       */
      width?: number;
      /**
       * Optional intrinsic height in pixels.
       */
      height?: number;
    };
  };
  /**
   * Two or three sentences that explain the collection’s value and scope without generic marketing language.
   */
  deck: string;
  /**
   * One to one hundred fully authored articles, with no more than 2,000,000 Markdown bytes combined. Articles may include structured card/hero images, article-specific Open Graph images, and Markdown body images. Read all in-scope source material before composing them; preserve distinctions, uncertainty, image provenance, and rights context instead of flattening the corpus.
   *
   * @minItems 1
   * @maxItems 100
   */
  articles: [
    {
      /**
       * Unique kebab-case article identifier.
       */
      slug: string;
      /**
       * Repeated section label used to group related articles in navigation.
       */
      category: string;
      /**
       * Short framing line above the article title.
       */
      kicker: string;
      /**
       * Reading order. Values must be unique.
       */
      order: number;
      /**
       * Article title that states the question, decision, or lesson.
       */
      title: string;
      /**
       * One or two sentences explaining what the reader will understand.
       */
      summary: string;
      /**
       * Optional source class such as "Conversation synthesis", "Research notes", or "Workshop guide".
       */
      sourceType?: string;
      /**
       * Visible provenance label naming the material this article was derived from. Do not invent a source.
       */
      sourceLabel: string;
      /**
       * Optional revision identifier or version label.
       */
      revision?: string;
      /**
       * Optional human-readable source update date.
       */
      updatedAt?: string;
      /**
       * Optional article image shown on cards and above the article body. Markdown images remain supported inside the body.
       */
      image?: {
        /**
         * Public HTTP(S) image URL.
         */
        url: string;
        /**
         * Required accessible description of the image.
         */
        alt: string;
        /**
         * Optional visible caption.
         */
        caption?: string;
        /**
         * Optional visible creator, publisher, or rights credit.
         */
        credit?: string;
        /**
         * Optional public HTTP(S) source page for provenance or rights context.
         */
        sourceUrl?: string;
        /**
         * Optional intrinsic width in pixels.
         */
        width?: number;
        /**
         * Optional intrinsic height in pixels.
         */
        height?: number;
      };
      /**
       * Optional article-specific social preview image. Defaults to article.image, then site.ogImage.
       */
      ogImage?: {
        /**
         * Public HTTP(S) image URL.
         */
        url: string;
        /**
         * Required accessible description of the image.
         */
        alt: string;
        /**
         * Optional visible caption.
         */
        caption?: string;
        /**
         * Optional visible creator, publisher, or rights credit.
         */
        credit?: string;
        /**
         * Optional public HTTP(S) source page for provenance or rights context.
         */
        sourceUrl?: string;
        /**
         * Optional intrinsic width in pixels.
         */
        width?: number;
        /**
         * Optional intrinsic height in pixels.
         */
        height?: number;
      };
      /**
       * Complete article body in Markdown. Standard Markdown images are allowed with descriptive alt text. Use H2/H3 headings for jump links, short paragraphs, concrete examples, and tables only where they improve comparison.
       */
      markdown: string;
    },
    ...{
      /**
       * Unique kebab-case article identifier.
       */
      slug: string;
      /**
       * Repeated section label used to group related articles in navigation.
       */
      category: string;
      /**
       * Short framing line above the article title.
       */
      kicker: string;
      /**
       * Reading order. Values must be unique.
       */
      order: number;
      /**
       * Article title that states the question, decision, or lesson.
       */
      title: string;
      /**
       * One or two sentences explaining what the reader will understand.
       */
      summary: string;
      /**
       * Optional source class such as "Conversation synthesis", "Research notes", or "Workshop guide".
       */
      sourceType?: string;
      /**
       * Visible provenance label naming the material this article was derived from. Do not invent a source.
       */
      sourceLabel: string;
      /**
       * Optional revision identifier or version label.
       */
      revision?: string;
      /**
       * Optional human-readable source update date.
       */
      updatedAt?: string;
      /**
       * Optional article image shown on cards and above the article body. Markdown images remain supported inside the body.
       */
      image?: {
        /**
         * Public HTTP(S) image URL.
         */
        url: string;
        /**
         * Required accessible description of the image.
         */
        alt: string;
        /**
         * Optional visible caption.
         */
        caption?: string;
        /**
         * Optional visible creator, publisher, or rights credit.
         */
        credit?: string;
        /**
         * Optional public HTTP(S) source page for provenance or rights context.
         */
        sourceUrl?: string;
        /**
         * Optional intrinsic width in pixels.
         */
        width?: number;
        /**
         * Optional intrinsic height in pixels.
         */
        height?: number;
      };
      /**
       * Optional article-specific social preview image. Defaults to article.image, then site.ogImage.
       */
      ogImage?: {
        /**
         * Public HTTP(S) image URL.
         */
        url: string;
        /**
         * Required accessible description of the image.
         */
        alt: string;
        /**
         * Optional visible caption.
         */
        caption?: string;
        /**
         * Optional visible creator, publisher, or rights credit.
         */
        credit?: string;
        /**
         * Optional public HTTP(S) source page for provenance or rights context.
         */
        sourceUrl?: string;
        /**
         * Optional intrinsic width in pixels.
         */
        width?: number;
        /**
         * Optional intrinsic height in pixels.
         */
        height?: number;
      };
      /**
       * Complete article body in Markdown. Standard Markdown images are allowed with descriptive alt text. Use H2/H3 headings for jump links, short paragraphs, concrete examples, and tables only where they improve comparison.
       */
      markdown: string;
    }[]
  ];
  /**
   * Optional download filename. The server always normalizes it to a safe .html filename.
   */
  filename?: string;
}

export interface Output {
  ok: boolean;
  title: string;
  filename: string;
  delivery: "artifact" | "local_file";
  articleCount: number;
  wordCount: number;
  bytes: number;
  sha256: string;
  generatedAt: string;
  artifact?: {
    artifactId: string;
    filename: string;
    contentType: "text/html";
    bytes: number;
    sha256: string;
    expiresAt: string;
    downloadUrl: string | null;
    downloadUrlExpiresAt: string | null;
  };
  localPath?: string;
  warnings: string[];
}
