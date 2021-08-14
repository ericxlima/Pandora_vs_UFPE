## For Commits, use this guide for "Semantic Commits"
#
### Structure:
```
<type>: <description>
```
### Types and Examples:
- __feat__: used when adding anything. 
    ```
    feat: add Pandora class
    ```
- __fix__: used when fixing code errors that are causing bugs
    ```
    fix: fixed menu error 
    ```
- __refactor__: used in performing a refactoring that will not have a direct impact
    ```
    refactor: all classes names for english names
    ```
- __style__: used when style changes are made.
    ```
    style: Pandora use mask now
    ```
- __test__: used when making changes of any kind to the tests
    ```
    test: collision tests
    ```
- __doc__: used when adding or modifying some documentation in the code or repository. 
    ```
    doc: all archives with documentation
    ```
- __build__: used when modifying dependency files
    ```
    build: we will use the package pygame-ia now for IA in enemies
    ```

#
### Pushing
- For working in this project:
```bash
#  Use this, for get a orientation
git status

# Go to the development branch
git checkout dev

# Update to the latest:
git pull

    #  Work on the project...

# Make a Semantic Commit
git add <files>  #  use a dot (.) if was more archives
git commit -m "<type>: <description>"

# Then, send it to the development branch:
git push origin dev
``` 