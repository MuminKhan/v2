### Submission

Note: I moved the old `README.md` to [setup.md](setup.md) to take advantage of GH's markdown rendering for this submission. 

1. How much disk space is used after step 4?
```
[root@ip-172-31-39-129 gpfsfpo]# df -h
Filesystem      Size  Used Avail Use% Mounted on
devtmpfs        1.9G     0  1.9G   0% /dev
tmpfs           1.9G     0  1.9G   0% /dev/shm
tmpfs           1.9G   33M  1.9G   2% /run
tmpfs           1.9G     0  1.9G   0% /sys/fs/cgroup
/dev/xvda1      100G  6.4G   94G   7% /
tmpfs           379M     0  379M   0% /run/user/1000
gpfsfpo         300G  6.1G  294G   3% /gpfs/gpfsfpo
```
2. Did you parallelize the crawlers in step 4? If so, how? 
    * No, I did not
3. Describe the steps to de-duplicate the web pages you crawled.
    * I did not have to do this, as the crawlers were not parallelized 
4. Submit the list of files you that your LazyNLP spiders crawled (ls -la).
    * I have included [aus_gutemberg_dataset.txt](aus_gutemberg_dataset.txt) and [reddit.txt](reddit.txt) for this submission. The Wikipedia URL list 404's as noted in `crawler.py`