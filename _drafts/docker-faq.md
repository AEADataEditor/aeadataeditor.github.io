These are good questions, and I might steal some of these for an FAQ in the future!

>   When creating an image and installing some Linux packages we will use the version available on the date we are creating the image and not the date the docker file was created or the code was originally run. This can pose replicability issues. It is possible to pin Linux packages, but it is not the usual practice for docker files.

I agree, but: The docker file is the transparency component, it is not necessarily the fully reproducible script, for precisely this issue. Linux packages are not the only ones that are an issue (Stata as well!). Pinning Linux packages is hard, because the reliance is typically on the (sparse) open package repositories. This might be better controlled within a controlled environment like yours.

> Versioning of packages should be enforced in the scripts.

To the extent possible, yes. Caveats for "standard" Linux package installs - that's not obvious

> I would recommend adding a section on the use of hash codes to ensure that the data used is the same as that available on the date it is used to replicate the study.

the use of hash codes is definitely not part of the general canon, so that is not pedagogically useful here. Also, the Docker images I usually create (that most people create) do NOT integrate the data. This is part of what the user-level code needs to do. But there is no commonly accepted way of doing so (to wit: "dvc" is not part of the standard Linux repositories...)

> As an additional precaution, I would recommend the authors keep a replica of the image of the Docker container at DockerHub and the Singularity container at Sylabs (one can build the singularity def file at https://cloud.sylabs.io/home and share the resulting image).

Not the point of the blog post, but I agree mostly. I actually do NOT suggest keeping the replica on DockerHub. That's as fallible as Github. The correct way is to export the container as a Tar file, and store that on Zenodo or another trusted repository. There is a standard for containers, and it is NOT necessary to store the singularity version of it, as singularity can ingest a Docker export.

> From our experience at BPLIM, I would also include Singularity containers as a major option.

I point to them in the blog post, but the blog post is about docker, not singularity, for the sake of simplicity. Neither are widely available, and there are others as well (podman, smaller fry)

> Advantages of Singularity include an easier integration with the filesystem (by default docker isolates as much as possible the container). This is particularly relevant when you run the container in a safe centre as is the case of BPLIM where data is located outside the container.

This statement is wrong. "Easier integration with the filesystem" is a weakness from a security perspective. Plus, Docker can map anything from your local filesystem into the container, see my example scripts.

> In this specific environment, the fact that docker also isolates the user ID may create difficulties interacting with the localhost -> This is particularly relevant under Linux as the output is owned by root -> As this may raise security issues, the IT department at the bank only allows singularity containers in the servers.

This statement is wrong, but the solution is non-trivial. One can run docker "root-less" and one can map user ids into the container. There are also other workarounds.

That being said, the various IT departments across secure environments will always come to different solutions, so there need to be multiple approaches. The fundamental container approach is independent of docker/singularity/podman/etc. .

> It may be interesting to mention GESIS Notebooks as a repository for Bynder images and Google Cloud Shell (one can install singularity in our container in google could platform).

There are hundreds of container-based solutions out there. Every single one of the major cloud vendors, plus all the revendors, plus value-added services allow you to run containers (sometimes called apps), sometimes run containers but hide it away from you.

I did take note of the GESIS notebooks, not because of docker, but because of the fact that there are few places to properly archive notebooks. This might be one.

> A side note. From my own experience, I can't always create an image from the docker file on a computer with the M1 processor. In other words, with technological evolution (new processors) there is no guarantee that in some years we will be able to recreate these containers. There's always the possibility of virtual machines, but it's an added complexity.

Not entirely correct. macOS never runs containers natively, because fundamentally, containers are Linux systems. Containers also do not run natively on Windows. That has nothing to do with the processor, and everything to do with capabilities of the OS (many VM solutions also initially failed on M1 processors). Fundamentally, Docker on macOS and on Windows runs in a Virtual Machine hosting Linux. But that VM is standardized, and made to be as efficient as possible by the OS vendor (or the Docker/Singularity folks). If you can run Linux on mac or Windows, you can run singularity (maybe docker) without vendor support. If you can't, then it doesn't work. That is not a fundamental problem: containers are fundamentally not meant to run on desktop (developer) machines at production level quality. They are meant to run in the cloud.

But that means that the layer the user specifies (container) is "light", all the heavy lifting is done by the software. Because containers are a fundamental building block of the broader web economy, they continue to be well-maintained, and developers continue to be supported. You can be assured that the M1 problem has a solution, not because a bunch of economists wants to run it, but because every major software development company with thousands of developers need it to work...

## Computing in the Cloud

From easy to complex/sophisticated solutions, all except for the bare-bones cloud resources.

- https://codeocean.com/: 10h free with academic email - Matlab, Stata, and any of the usual open source things
- https://wholetale.org/ : free. Can use Google or ORCID to sign up. Matlab, Stata, and the usual open source things
- https://github.com/features/codespaces  : up to 32 core/64GB RAM for pennies per hour. I think it requires you to have a Github Pro subscription or be part of an 'organization'. Base is $4/month, plus compute/storage costs. A bit more setup, but easy enough - here's one with Stata enabled that I created. It is even easier with R.
- https://www.paperspace.com/ Starts to be a bit more complex, but works. $
- https://www.digitalocean.com/ also has easy to use "droplets", there's even a R package to run it from local to cloud: https://www.r-bloggers.com/2015/05/teaching-r-course-use-analogsea-to-run-your-customized-rstudio-in-digital-ocean/
- Google Colab



    "Sharing" (but not preserving) images can be done via Docker Hub. Other container registries exist as well - Microsoft (Azure), Github, Google Cloud all have docker registries. A comparable service is for Singularity images.
    Preserving containers can be done by exporting them into TAR files, then using Zenodo etc. to preserve them. They can be large! See https://docs.docker.com/engine/reference/commandline/save/ for Docker commands. That should be the primary​ way of preserving it for the journal!
    Containers are "opaque" - they hide what's in them, similar to simply posting a ZIP file of "stuff". It is not efficient to store 100kB of Matlab code in a 5GB container that is tarred up. People do not NEED docker to run Matlab + Dynare scripts (but it is convenient). So my recommendations (which I submit as "draft our" recommendations) is that
        the container image is auxiliary in the sense that it contains all software (here: Matlab + Dynare), but none of the scripts and data. In other words, the script and data should be "mounted" into the image, not copied into the image. See https://solutions.posit.co/envs-pkgs/environments/docker/#code for an example. 
        the replication package should STILL have instructions on what software is needed (i.e., Matlab + Dynare)
        it should be feasible to download the Matlab + dynare code separately (possibly: two different Zenodo archives, but definitely not a monolithic TAR or ZIP file on Zenodo, since you can't download individual files out of Zenodo-hosted ZIP file).
        full instructions on how to (command line) run the Docker image should be provided as part of the README (e.g. "docker -v /path/to/code:/code -v /path/to/data:/data image/paperdocker")
    There is an official Matlab container https://www.mathworks.com/help/cloudcenter/ug/matlab-container-on-docker-hub.html which ideally serves as base for what this author has constructed as a container. Note that it must install any needed toolboxes - it comes without any! Alternatively, you could use the Matlab container provided by CodeOcean (which does have toolboxes installed). The Mathworks page above has the command line needed to run with a license. Careful: the container MUST NOT contain the author's license file... (they are responsible for it. You can test by running the container without feeding it a license, if it works, well, they installed it...) Not including a license is not easy - it should not be in any of the layers, ever... 

Put differently, one thing that Joan's RA should do is to test if Matlab + Dynare code can be run without the container. It should - it's a pretty standard setup - and that's what's really important for reproducibility and replicability by others.