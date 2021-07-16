From https://www.cross-validated.com/Personal-website-with-Minimal-Mistakes-Jekyll-Theme-HOWTO-Part-I/

    docker build -t ruby-environment . -f Dockerfile.init

then

    docker run --volume="$PWD:/usr/src/app" -it ruby-environment bundle install

then build a container specifically for the website:

    docker build -t aeaweb . -f Dockerfile.step2
    docker run --volume="$PWD:/usr/src/app" -p 4000:4000 -it aeaweb

To enable Github variables,

- Generate token: https://github.com/settings/tokens
- Stick it into $HOME/Dropbox/.myconfig/github-docker-secret
- Make that location the env variable "key"
- Include 

  JEKYLL_GITHUB_TOKEN=$(cat $key) 

in your Jekyll environment, for instance passing it with "-e" to the docker environment.



