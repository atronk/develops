# develops news feed API

How to build the API:

    Make sure docker and docker-compose are installed on the system, or refer to these links for installation guide:

    https://docs.docker.com/compose/install/
    https://docs.docker.com/get-docker/

    Clone the repository with: git clone https://github.com/artpheon/develops.git

    If using Linux you may need to start the docker with: sudo systemctl start docker

    Change directory to the cloned repository, and once inside, execute:

     docker-compose up

or add 'sudo' in the beginning.

    The API will be available at http://0.0.0.0:8000/api/ in the browser

Some of the API functionality:

GET all posts: /api
GET specific post: /api/*id*
GET comments: /api/*id*/comments
