import BackendPath from "./backend_path";

const homeRequest = async () => {
    return await fetch(BackendPath.HOME);
}

export default homeRequest;