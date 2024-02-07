const baseUrl = "http://127.0.0.1:8000/api/v1/"

const BackendPath = Object.freeze({
    HOME: baseUrl + "home/",
    SEASON_COUNT: baseUrl + "seasons-list/count/",
    SEASON_DATA: baseUrl + "seasons-list/?season=0",
    CHARACTERS: baseUrl + "character/?"

});

export default BackendPath;