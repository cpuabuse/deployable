# Globals
tab = "  "

# Help
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
