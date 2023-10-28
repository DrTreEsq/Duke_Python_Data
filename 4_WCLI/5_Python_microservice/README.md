# functions-from-zero
live training

[![Python application test with Github Actions](https://github.com/noahgift/functions-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/noahgift/functions-from-zero/actions/workflows/main.yml)


### To call Microservice 

something like this
```bash
curl -X 'POST' \
  'https://noahgift-functions-from-zero-r7g59wcxx6x-8080.githubpreview.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft"
}'
```

### Build container

`docker build .`
`docker image ls`

### Run container

something like this

`docker run -p 127.0.0.1:8080:8080 a81ce4f35866`

### Invoke POST request

run `invoke.sh`

## References

* [Watch Walkthrough on YouTube](https://youtu.be/KOAdCqpQSI4)

Run a Microservice

In this lab you will do the following:  

1.  Run python main.py

###### there are steps before this - does not pop up automatically, not for regular browser app
2.  Open the browser preview and type in 127.0.0.1:5050/add/2/2


3.  Verify you can add numbers with this microservice

4.  Experiment with adding a new route that multiplies numbers.


###### You can review an example here:  https://github.com/noahgift/functions-from-zero

###### You can review a what this process look like here:  https://user-images.githubusercontent.com/58792/160030338-de954b2c-8ab2-4980-a459-e512000bb0dd.png


