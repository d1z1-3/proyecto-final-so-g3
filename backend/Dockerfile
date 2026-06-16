FROM fedora:41
RUN dnf update -y && dnf install -y python3
WORKDIR /app
COPY server.py .
EXPOSE 5000
CMD ["python3", "server.py"]
