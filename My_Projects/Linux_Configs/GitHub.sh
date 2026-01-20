#How to synchronize a local directory with a GitHub repository
#Usage: ./GitHub.sh /path/to/local/directory
#!/bin/bash
LOCAL_DIR=$1
if [ -z "$LOCAL_DIR" ]; then
  echo "Usage: $0 /path/to/local/directory"
  exit 1
fi
if [ ! -d "$LOCAL_DIR/.git" ]; then
  echo "The specified directory is not a Git repository."
  exit 1
fi
cd "$LOCAL_DIR" || exit 1
git add .
git commit -m "Automated commit: $(date +"%Y-%m-%d %H:%M:%S")"
git push origin main
echo "Local directory synchronized with GitHub repository." 
exit 0  
##################################################
#End of GitHub.sh
##################################################
##################################################
#Script Name: GitHub.sh
#Description: Synchronizes a local directory with a GitHub repository by adding, committing, and
#             pushing changes.
#Usage: ./GitHub.sh /path/to/local/directory
    