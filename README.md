## py-nudec

__py-nudec__ (python nude detector) is a microservice, which scans all the images and videos from the multipart/form-data request payload and sends a response with a boolean value which indicates if all content has passed the checks.

This service uses [NudeNet](https://github.com/notAI-tech/NudeNet) created by [notAI-tech](https://github.com/notAI-tech)

## Configuration

To start the service run the `run` command:

```bash
make run
```

This will install all the necessary dependencies and will start the service.

## Endpoint for checking

`/analyze` route that accepts POST requests and multipart/form-data information. which returns a true or flase.
`/detect` route that accepts POST requests and multipart/form-data information, which returns a ratio of safe and unsafe.
