From https://www.cross-validated.com/Personal-website-with-Minimal-Mistakes-Jekyll-Theme-HOWTO-Part-I/

    docker build -t ruby-environment .

then

    docker run --volume="$PWD:/usr/src/app" -it ruby-environment bundle install

then build a container specifically for the website:

    docker build -t aeaweb .
    docker run --volume="$PWD:/usr/src/app" -p 4000:4000 -t aeaweb

