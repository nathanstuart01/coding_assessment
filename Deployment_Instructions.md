## Instructions to setup Flask Movie App

### Datasets

Navigate to `https://datasets.imdbws.com` and download the following datasets:

- `title.basics.tsv.gz` - Dataset of imdb titles.
- `title.ratings.tsv.gz` - Dataset of imdb ratings.

### Prepare the data

#### Unzipping

To unzip the gz files, you can use this command:

`gzip -d <filename>`

Reference: `https://linuxize.com/post/how-to-unzip-gz-file/`

#### Renaming and Moving

To make the data available for use by the app, do the following:

1. Rename the unzipped `title.basics.tsv.gz` file to `basics_data.tsv`:

`mv /path/to/file/title.basics.tsv.gz /path_to_file/basics_data.tsv.gz`

2. Rename the unzipped `title.ratings.tsv.gz` file to `ratings_data.tsv`:

`mv /path/to/file/title.basics.tsv.gz /path/to/file/ratings_data.tsv`

3. Move the unzipped file `basics_data.tsv` to the root directory of this app:

`mv /path/to/file/basics_data.tsv /path/to/code/coding_assessment/basics_data.tsv`

4. Move the unzipped file `ratings_data.tsv` to the root directory of this app:

`mv /path/to/file/ratings_data.tsv /path/to/code/coding_assessment/ratings_data.tsv`

### App Deployment Requirements

To deploy the app to your local machine do thhe following:

1. Install Docker:

`https://docs.docker.com/get-docker/`

2. Navigate to root directory of this app:

`cd /path/to/code/coding_assessment/`

3. Build Docker image:

`docker build -t name_of_image:version_of_image .`

4. Run Docker image as a container:

`docker run --rm --name name_of_app_to_use -p 8000:5000 name_of_image:version_of_image`

### API Endpoint Information

#### Endpoint 1: /count_movie_titles_genres

Request Type:
`GET`
Headers Requrired:
`Content-Type: application/json`
Request Data Required: The follownig data is requrired to make a successful request:
`{"genre":"genre_you_want_to_get_count_for"}`
Request Data Returned: The following data is returned in JSON format:
`{'Genre': genre_you_provided, 'Count Movie Titles': genre_you_provided_count}`
Status Code if successful:
`200`
Example Curl Call to Test Endpoint:
`curl -i -X GET -H "Content-Type: application/json" -d '{"genre":"Genre you want to get count for"}' http://127.0.0.1:8000/ count_movie_titles_genres`

#### Endpoint 2: /get_movie_title_rating

Request Type:
`GET`
Headers Requrired:
`Content-Type: application/json`
Request Data Required: The follownig data is requrired to make a successful request:
`{"title":"title_you_want_to_get_rating_for"}`
Request Data Returned: The following data is returned in JSON format:
`{'Title': title, 'Avg Rating': movie_rating }`
Status Code if successful:
`200`
Example Curl Call to Test Endpoint:
`curl -i -X GET -H "Content-Type: application/json" -d '{"title":"title_you_want_to_get_rating_for"}' http://127.0.0.1:8000/get_movie_title_rating`

#### Endpoint 3: /get_top_rated_movie_genre

Request Type:
`GET`
Headers Requrired:
`Content-Type: application/json`
Request Data Required: The follownig data is requrired to make a successful request:
`{"genre":"genre_you_want_to_find_top_rating_for"}`
Request Data Returned: The following data is returned in JSON format:
`{'Genre': genre, 'Top Rated Title(s)': top_rated_title})`
Status Code if successful:
`200`
Example Curl Call to Test Endpoint:
`curl -i -X GET -H "Content-Type: application/json" -d '{"genre":"Genre you want to find top rating for"}' http://127.0.0.1:8000/get_top_rated_movie_genre`

## Questions

Please email `nathanstuart01@gmail.com` if you have any questions about how to use this app
