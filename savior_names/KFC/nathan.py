# %%
import pyarrow
import polars as pl
import re

# %%
# Load data
lds_scripture = pl.read_csv("lds-scriptures.csv")
savior_names = pl.read_parquet("../BoM_SaviorNames.parquet")

# Filter to Book of Mormon
lds_scripture = lds_scripture.filter(pl.col("volume_lds_url") == "bm")

# %%
# Get savior names
savior_names = savior_names.select(["name"])
savior_names = savior_names["name"].to_list()


# %%
# Define function to process verses
def process_verses(df, savior_names):
    data = []
    specific_words = [
        "a",
        "an",
        "and",
        "are",
        "as",
        "at",
        "be",
        "but",
        "by",
        "for",
        "if",
        "in",
        "into",
        "is",
        "it",
        "no",
        "not",
        "of",
        "on",
        "or",
        "such",
        "that",
        "the",
        "their",
        "then",
        "there",
        "these",
        "they",
        "this",
        "to",
        "was",
        "will",
        "with",
    ]

    for row in df.to_dicts():
        verse_text = row["scripture_text"]
        book = row["book_title"]
        chapter = row["chapter_number"]
        verse = row["verse_number"]

        for name in savior_names:
            if name in verse_text:
                words_after_name = re.split(rf"\b{name}\b", verse_text, 1)[-1].strip()
                words_after_list = words_after_name.split()
                num_words_after = len(words_after_list)

                word_counts = {
                    word: words_after_list.count(word) for word in specific_words
                }
                num_verses_covered = 1  # Since each row corresponds to a single verse

                data.append(
                    {
                        "book": book,
                        "chapter": chapter,
                        "verse": verse,
                        "words_after_name": words_after_name,
                        "num_words_after": num_words_after,
                        "num_verses_covered": num_verses_covered,
                        **word_counts,
                    }
                )

    return pl.DataFrame(data)


# Process the verses
processed_data = process_verses(lds_scripture, savior_names)


# %%
# Show the processed data
processed_data

# %%
