"""
Defaults for deployable package.
"""

from deployable.environment.defaults import file_id, types # For constructing help
from os import sep # For constructing paths

# Default paths
default_config_path = "deploy.yml"
default_environment_path = f".{sep}"

# Argsparse args
tab = "  "
description = f"""\
description:
{tab}Automates deployment
{tab}cpuabuse.com 2019\
"""
epilog = f"""\
examples:
{tab}1) deploy file ".deployable.yml" located in current directory:

{tab}{tab}deployable

{tab}2) deploy files "a.deployable.yml" and "b.deployable.yml":

{tab}{tab}deployable -c a.deployable.yml b.deployable.yml\
"""

def get_help(text):
	"""
	Provides help text.
	"""
	override_flags_separator = "\", \""
	override_flags = [f"--{type_item}" for type_item in types] + ["--type"]
	help_text = {
		"config" : f"""\
location of the configuration file(s);
defaults to "{default_config_path}"\
""",
		"dry" : "the stages would not execute, only evaluate the directives",
	"environment" : f"""\
the path for the environment to execute;
defaults to the directory of the config file(s);
if config files are not provided, or have different directories, defaults to "{default_environment_path}"\
""",
		"type" : f"""\
types of config;
if less arguments than "--config" is provided, rest would default to "{file_id}";
if more arguments than "--config" is provided, rest would be ignored;
cannot be used at the same time as "{override_flags_separator.join([i for i in override_flags if i != "--type"])}"\
"""
	}
	if text in help_text:
		return help_text[text]	
	else:
		if text in [type_item for type_item in types]:
			return f"""\
forces config to be treated as {types[text]["name"]}(s);
cannot be used at the same time as "{override_flags_separator.join([i for i in override_flags if i != f"--{text}"])}"\
"""
	
	# Finally return if failed
	return "help text not defined"