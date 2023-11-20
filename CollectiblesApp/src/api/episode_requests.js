import BackendPath from "./backend_path"

const getEpisodesCountRequest = async () => {
    return await fetch(BackendPath.EPISODES_COUNT);
}

export { getEpisodesCountRequest };