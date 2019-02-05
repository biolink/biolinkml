docker run --rm -d -p $1:80 --name httptest -v $(pwd)/w3id.org/:/usr/local/apache2/htdocs/ http_test
