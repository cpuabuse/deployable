# Specification for the deployment configuration

Deployment configuration is a file written in YAML 1.2 with a `.deployable.yml` extension.

## Syntax

### Stage

Stage is an object, member of `stage` array in the root of the deployment configuration.

1. The stage contains primary and secondary directives as properties.
1. The first directive of the stage is a primary directive.

## Design guidelines

### Options

1. The default values for all the options are to be assumed.

### Stages

1. The stage should be executable with only a primary directive, where the value is of type string.
1. The secondary directives should have separate functionality from the primary directive itself. For example, for `publish_file` primary directive, the value for `publish_file` is to be a file path. Adding `file2` directive for second file to publish, should not be done. Iterations should be implemented isntead.
1. The stage should process only one primary directive, while others should be ignored.
1. The directive keys should be short and simple.
