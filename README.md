# "Rick and Morty" application
It's not fully implemented, but there are implemented main features:
- RESTful API with Token & Session Authentication
- Some simple frontend to visualize data
- scrapper to scrap data from [RickAndMortyApi](https://rickandmortyapi.com/)

## API endpoints
### Auth
- 'api/v1/sign-up/'
- 'api/v1/sign-in/'
- 'api/v1/logout/'
- 'admin/' - only for admin to manipulate with data
### Scraped data
- 'api/v1/location/' - to get locations from the RickAndMorty multiverse
- 'api/v1/character/'- to get characters from the RickAndMorty multiverse
- 'api/v1/episode/' - to get episodes from the RickAndMorty multiverse
- 'api/v1/seasons-list/'- to get episodes grouped by seasons
### Collections
- 'api/v1/usercard/' - to work with users collected cards
- 'api/v1/collection/<user>' - to see user's collection
- 'api/v1/me/' - to get data about current user
- 'api/v1/home/' - to get random 4 characters for home page

## Tech Stack
### Backend: *Python, Django, DRF, PostgreSQL*
### Frontend: *React, JS*
#### To start this app:
1. Clone repo
2. Create .env file using .env.example
3. Set also .env file for docker compose file
4. Run command to build and start docker images 

``` bash
docker compose up --build
```
5. Open scrapper_backend_web_container bash, and make migration
6. *Optional* Run special command to start scrapping process
    - It can take some time to execute

``` bash
python manage.py scrap
```
