# -----------------------------Positional-Only Parameters

# Looking at this in a bit more detail, it is possible to mark certain parameters as positional-only.
# If positional-only, the parameters’ order matters, and the parameters cannot be passed by keyword.
# Positional-only parameters are placed before a / (forward-slash). The / is used to logically
# separate the positional-only parameters from the rest of the parameters. If there is no / in the
#  function definition, there are no positional-only parameters.

# Parameters following the / may be positional-or-keyword or keyword-only.
# position_only_arg is restricted to only use positional parameters as there is a / in the
# function definition:

def Position_only_arg(arg, /):
	print(arg)

Position_only_arg('Equal')
# Position_only_arg(arg="equla")  # give Error