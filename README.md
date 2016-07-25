# ansible-java

An Ansible role for installing Java.

## Role Variables

- `java_version` - Java JDK and JRE version
- `java_major_version` - Major version of Java to install (default: `7`)
- `java_flavor` - Flavor of Java to install (default: `openjdk` but can also be `oracle`)
- `java_oracle_accept_license_agreement` - Flag to accept the Oracle license agreement (default: `False`)

## Testing
Tests are done using [molecule](http://molecule.readthedocs.io/). To run the test suite, install molecule and its dependencies and run ` molecule test` from the folder containing molecule.yml. To add additional tests, add a [testinfra](http://testinfra.readthedocs.org/) python script in the [tests](./tests/) directory, or add a function to [test_java.py](./tests/test_java.py). Information about available Testinfra modules is available [here](http://testinfra.readthedocs.io/en/latest/modules.html).

### Example 
```
# Download molecule, dependencies
$ pip install molecule

# Change to the top-level project directory, which contains molecule.yml
$ cd /path/to/ansible-java

# Ensure that molecule.yml is present
$ ls
CHANGELOG.md                             molecule.yml
LICENSE                                  playbook.retry
README.md                                playbook.yml
ansible.cfg                              tasks
defaults                                 templates
handlers                                 tests
meta                                     

# We're in the right directory, so let's run tests!
$ molecule test

```
