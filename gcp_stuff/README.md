#### Create gcloud CLI configuration
gcloud config configurations create [config-name]


#### Activate configuration for CLI
gcloud config configurations activate [config-name]


#### Initialise account
gcloud auth login


#### Set gcloud account
gcloud auth list
gcloud config set account [my-account@example.com]


#### Set default gcloud project (not recommended)
gcloud config set project my-project-id


#### View default gcloud project
gcloud config list --format 'value(core.project)' 2>/dev/null
