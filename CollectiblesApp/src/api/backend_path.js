const baseUrl = "http://127.0.0.1:8000"

const BackendPath = Object.freeze({
    HOME: baseUrl + "/home/",
    SEASON_COUNT: baseUrl + "/api/seasons-list/count/",
    SEASON_DATA: baseUrl + "/api/seasons-list/?season=0"
});

export default BackendPath;