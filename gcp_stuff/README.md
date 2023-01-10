#### Set gcloud account
gcloud auth list
gcloud config set account `ACCOUNT`


#### Set default gcloud project
gcloud config set project omega-s


#### View default gcloud project
gcloud config list --format 'value(core.project)' 2>/dev/null

### Manage gcloud cli Config

#### Create configuration
gcloud config configurations create [config-name]


#### Activate configuration for CLI
gcloud config configurations activate [config-name]


#### Set project
gcloud config set project my-project-id


#### Initialise account
gcloud auth login


#### Set account
gcloud config set account [my-account@example.com]


--- done
