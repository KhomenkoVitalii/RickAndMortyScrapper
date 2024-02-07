import BackendPath from "./backend_path"

const getSeasonsCountRequest = async () => {
    return await fetch(BackendPath.SEASON_COUNT);
}

const getSeasonEpisodesRequest = async (number) => {
    const URL = BackendPath.SEASON_DATA + number;
    console.log(URL);
    return await fetch(URL);
}

export { getSeasonsCountRequest, getSeasonEpisodesRequest };