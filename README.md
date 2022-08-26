# Nasdaq-New-Scraper

<h3>Enter Ticker/Symbol and get the news</h3>

<h2>Step 1</h2>

Just run the **docker-compose.yml** with:

```
docker-compose up
```


<h2>Step 2</h2>
After that, point your web browser at 


 ` http://127.0.0.1:8000/news/<ticker> ` or `localhost:8000/news/msft`
---

**Here < ticker > is msft** ``MSFT``

<img width="500" alt="Screenshot 2022-08-27 at 3 56 55 AM" src="https://user-images.githubusercontent.com/92709590/186998534-51920c57-4ab0-486a-854a-2410a719d433.png">

After a successful run,   **Done!** message will display on your web page, it means our news has been fetched and saved successfully.

<h2>Step 3</h2>

To check whether the news data has been stored or not, parallely open a new terminal and invoke the redis cli of the container, use:

```
docker exec -it <up container-name> redis-cli
```

Check the keys present using `keys *` and check the list using `lrange key 0 -1` you'll get something like this -->
<img width="800" alt="Screenshot 2022-08-27 at 4 14 46 AM" src="https://user-images.githubusercontent.com/92709590/186999858-492a3bb8-9b39-4dd6-aa3b-75f978b9a068.png">
