## Inspiration
Lately Facebook posts are increasingly loaded with links and we share a mutual hate for articles that misrepresent their content in the hope of attracting user clicks. This internet trend is deceptive and tedious, so we decided to do something about it.

## What it does
[ClickBlock](https://chrome.google.com/webstore/detail/clickblock/bgiafoodmnpnhoinjfhgkgepamghmonk) is a chrome extension that automatically detects click-bait articles in your Facebook feed. Articles identified as click-bait are highlighted in red, and have their title replaced to be a more accurate description. Additionally, the extension provides a summary of the article when the user hovers over it.

## How we built it
ClickBlock was built using a flask server that handles the processing and identification of articles. A chrome extension calls the server and replaces the appropriate content.

## Challenges we ran into
Initially, we tried to make calls to the server through the web page itself but ran into issues with https validation. Facebook uses https protocol and was blocking our requests to the server. To work around this issue, we delegated the calls to browser instead of the webpage.

While scraping data for training our classifier, we ran into issues with the New York times using async calls for displaying the articles. In order to solve this problem we, analysed the requests being made to identify the xhr call responsible for displaying article content, which we simulated in our scraper.

We also tried to implement our own article summarizer, but rapidly ran into issues with the quality of the summaries. Natural language processing is a large and complicated problem that we did not have enough time to solve during the hackathon.

## Accomplishments that we're proud of
Our team worked together cohesively despite all of our members being from different countries. The Chrome Extention is now available for free download at this [link](https://chrome.google.com/webstore/detail/clickblock/bgiafoodmnpnhoinjfhgkgepamghmonk).

## What we learned
We learned how to create a chrome extension, as well as how to use web scraping as an effective tool for obtaining useful data.

## What's next for ClickBlock
UI updates and improved article classification would provide the finishing polish for this project. Additionally, ClickBlock could transition to also grading the reliability of the news, not just the accuracy of the headlines.
