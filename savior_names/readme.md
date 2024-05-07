## Counting Savior names in scripture

### Background

In 1978 Susan Easton Black [penned an article](https://www.lds.org/ensign/1978/07/discovery?lang=eng) in the Ensign title *Even statistically, he is the dominant figure of the Book of Mormon.* which makes some statistical claims about the Book of Mormon. With our “string” skills we are going to check her result and build an improved statistic using using number of words between references.

### Tasks

- [ ] Get the scripture and savior name data into a Polars dataframe
  - [ ] Download the data from http://scriptures.nephi.org/downloads/lds-scriptures.csv.zip
  - [ ] Read in the `.csv` file that was in the zip file and examine the structure of the data
  - [ ] Parse the savior name data into a polars dataframe
- [ ] Address the __Class concepts/goals__ below
- [ ] build visuals (at least one) that shows the patterns of word distance between savior names by book in the Book of Mormon
- [ ] Create an `.qmd` file with 1-2 paragraphs summarizing your graphic that shows how the distance between Savior names is distributed across the Book of Mormon
- [ ] Compile your `.md` and `.html` file into your git repository

### Class concepts/goals

- Can we take stored data where the _unit of analysis_ is verse and convert the _unit of analysis_ to words that appear after a `savior name`?
- Can we build a target variable, the number of words after a savior name?
- Can we build the following features - book where the name appears, chapter when the name appears, verse where the name appears, the number of times that `a, an, and, are, as, at, be, but, by, for, if, in, into, is, it, no, not, of, on, or, such, that, the, their, then, there, these, they, this, to, was, will, with` appear in the word block.

### Completion Structure

Follow these guidelines:

- Work with your team to get as far as possible in the hour.
- Use polars (unless it will not work, but it should).
- Each student submits their compiled report (which can be the teams) in Canvas.
- Each team submits a pull request by 3:30 pm on Tuesday. Please include a team folder within the savior name folder.
