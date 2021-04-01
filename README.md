# Python Engineer Coding Assessment

## Instructions

### Datasets

Navigate to [https://datasets.imdbws.com/]() and download the following datasets:

- `title.basics.tsv.gz` - Dataset of imdb titles.
- `title.ratings.tsv.gz` - Dataset of imdb ratings.

### Prepare the data

#### Unzipping

To unzip the gz files, you can use this command:

`gzip -d <filename>`

Reference: [https://linuxize.com/post/how-to-unzip-gz-file/]()

#### Data details

The `title.basics.tsv.gz` dataset contains many types of media, e.g. movies, tv episodes, shorts. For the purposes of
this assessment we will only be focusing on **MOVIES**.

### Requirements

For this assessment we will be evaluating your ability to build an api service using Flask and run it within a Docker container you provide the image for.

Please be prepared to answer questions about your code after submission.

There are three API endpoints we are requesting you to create:

#### Endpoint 1: Count all movie titles matching a given genre.

Details: Some movies have multiple genres. So long as the provided genre is among those genres, the title should be counted.

E.g.: `Comedy` should return `98267`

#### Endpoint 2: Given a movie title, provide the rating.

Details: You will need to handle these edge cases:

- The provided movie title does not exist.
- The provided movie title does not have a rating.

E.g.: `Call of the Yukon` should return `5.4`.

#### Endpoint 3: Given a genre, provide the top rated movie title for that genre.

E.g.: `Drama` should return `Amor fatal`.

#### Constraints

You must create 3 Flask endpoints that provide the above required services. All design decisions are up to you.
Errors must be handled (i.e. invalid user values).
Performance optimization is not required, however excessively slow responses will be noted. Please provide
instructions in a `DOC.md` on how to use your endpoints (i.e. POST, GET, query/path parameters, etc.)

## Docker

Please create a Docker image to deploy your code.

## Questions
Please email karol@ulap.co if you have any questions about the assessment.
