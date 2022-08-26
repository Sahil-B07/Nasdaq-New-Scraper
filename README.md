# Nasdaq-New-Scraper

<h3>Enter Ticker/Symbol and get the news</h3>

<h2>Step 1</h2>

Just run the **docker-compose.yml** with:

<img width="800" alt="Screenshot 2022-08-27 at 5 20 39 AM" src="https://user-images.githubusercontent.com/92709590/187004888-f4243387-4f51-4e5e-a362-11ba115631eb.png">

```
docker-compose up
```

**Success!** message will display on your terminal, it means our news has been fetched and saved successfully.

<h2>Step 2</h2>

To check whether the news data has been stored or not, parallely open a new terminal and invoke the redis cli of the container, use:

```
docker exec -it <up container-name> redis-cli
```

Check the keys present using `keys *` and check the list using `lrange key 0 -1` you'll get something like this -->


<img width="800" alt="Screenshot 2022-08-27 at 5 20 57 AM" src="https://user-images.githubusercontent.com/92709590/187004908-445fb44e-e0ef-4c18-b2e1-5047de5b737a.png">

