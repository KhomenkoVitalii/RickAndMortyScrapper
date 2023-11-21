import BackendPath from "./backend_path"

const getCharacters = (page) => {
    const URL = BackendPath.CHARACTERS + `?page=${page}`
    return fetch(URL);
}

export { getCharacters };