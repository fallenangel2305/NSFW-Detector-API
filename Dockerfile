FROM ubuntu


RUN apt update -y

RUN apt-get install -y python3.9 python3-pip



# Install `make` and `pipenv`
# RUN apt install build-essential pipenv -y

WORKDIR /app 
COPY . .
RUN pip3 install -r requirements.txt
# Default flask
EXPOSE 5000

# Start



RUN apt-get install wget -y

CMD ["cd","../../root/.NudeNet"]
CMD ["wget","https://nftstorage.link/ipfs/bafybeielkqplw7jbn2s4zcrlfw2jdu42fzi7kqcwqnxm2g4missnrtpfh4"]
CMD ["mv", "bafybeielkqplw7jbn2s4zcrlfw2jdu42fzi7kqcwqnxm2g4missnrtpfh4", "detector_v2_default_checkpoint.onnx"]
CMD ["mv", "bafybeib3p6kzzb2euisskdug5e2dpi7zw3b7o6njkazgqgbtnzqekekds4", "classifier_model.onnx"]
CMD ["mv","bafkreieq5uhact3e5uo66vrpsv34m3entg7fstu7f5ki4vfkfq44hpg4be","classes"]
CMD ["cd","../../app"]
CMD ["python3","-m","flask","run","--host=0.0.0.0"]

CMD [ "python3","-m","flask","run","--host=0.0.0.0" ]