async function getFeedFromSource(endpoint, keyword) {
    const response = await fetch(`${endpoint}?keyword=${keyword}`, {});
    const json = await response.json();
    return json;
}

async function getFullFeed (keyword) {
    const sources = [
        "http://127.0.0.1:5000/reddit",
        "http://127.0.0.1:5000/guardian",
        "http://127.0.0.1:5000/nyt",
        // "http://127.0.0.1:5000/crypto-panic"
    ]
    
    const feed = []

    sources.forEach(async function(source) {
        await getFeedFromSource(source, keyword)
        .then((redditFeed) => {
            for (entry in redditFeed) {
                feed.push(redditFeed[entry]);
            };
        });
    })
    return feed
}

removeAllChildren = (div) => {
    while (div.firstChild) {
        div.removeChild(div.firstChild);
    };
};

const searchBtn = document.querySelector("#search-btn");

searchBtn.addEventListener("click", () => {
    const input = document.querySelector("#search");
    console.log(input.value);
    getFullFeed(input.value)
    .then(data => {
        populate(data);
    });
});

let populate = (data) => {
    const resultsDiv = document.querySelector(".results")
    removeAllChildren(resultsDiv);
    console.log(data);
    for (entry in data) {
        console.log(data[entry])
        let header = document.createElement("h1").innerText = entry.title;
        resultsDiv.appendChild(header);
    };
};
