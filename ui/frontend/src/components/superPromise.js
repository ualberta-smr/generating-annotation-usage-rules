export default function makeCancellablePromise(url, jsonCallback) {
    let stop = false;
    const cancel = () => (stop = true);
    fetch(url)
        .then((r) => {
            if (stop === true) {
                throw new Error("Stop requested");
            }
            if (r.status >= 200 && r.status <= 206) return r.json();
            return null;
        })
        .then((json) => {
            if (stop === true) {
                throw new Error("Stop requested");
            }
            jsonCallback(json);
        })
        .catch((ignored) => {});
    return { cancel };
}
