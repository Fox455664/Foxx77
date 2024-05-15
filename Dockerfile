FROM Fox455664/Foxx77:slim-buster

RUN git clone git clone https://github.com/Fox455664/Foxx77.git /root/WWWL5

WORKDIR /root/WWWL5

RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/WWWL5/bin:$PATH"

CMD ["python3","-m","WWWL5"]
