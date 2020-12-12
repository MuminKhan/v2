### Submission

Note: I moved the old `README.md` to [setup.md](setup.md) to take advantage of GH's markdown rendering for this submission. 

1. How much disk space is used after step 4?
    * Crawler is still running, will update
2. Did you parallelize the crawlers in step 4? If so, how? 
    * No, I did not
3. Describe the steps to de-duplicate the web pages you crawled.
    * I did not have to do this, as the crawlers were not parallelized 
4. Submit the list of files you that your LazyNLP spiders crawled (ls -la).
    * I have included [aus_gutemberg_dataset.txt](aus_gutemberg_dataset.txt) and [reddit.txt](reddit.txt) for this submission. The Wikipedia URL list 404's as noted in `crawler.py`