import dataclasses


def dataclasses_init_fn_with_kwargs(fields, frozen, has_post_init, self_name):
    # fields contains both real fields and InitVar pseudo-fields.

    # Make sure we don't have fields without defaults following fields
    # with defaults.  This actually would be caught when exec-ing the
    # function source code, but catching it here gives a better error
    # message, and future-proofs us in case we build up the function
    # using ast.
    seen_default = False
    for f in fields:
        # Only consider fields in the __init__ call.
        if f.init:
            if not (f.default is dataclasses.MISSING and f.default_factory is dataclasses.MISSING):
                seen_default = True
            elif seen_default:
                raise TypeError(f'non-default argument {f.name!r} '
                                'follows default argument')

    globals = {'MISSING': dataclasses.MISSING,
               '_HAS_DEFAULT_FACTORY': dataclasses._HAS_DEFAULT_FACTORY}

    body_lines = []
    for f in fields:
        line = dataclasses._field_init(f, frozen, globals, self_name)
        # line is None means that this field doesn't require
        # initialization (it's a pseudo-field).  Just skip it.
        if line:
            body_lines.append(line)

    # Does this class have a post-init function?
    if has_post_init:
        params_str = ','.join(f.name for f in fields
                              if f._field_type is dataclasses._FIELD_INITVAR)
        body_lines.append(f'{self_name}.{dataclasses._POST_INIT_NAME}({params_str}{", " if params_str else ""} **kwargs)')

    # If no body lines, use 'pass'.
    if not body_lines:
        body_lines = ['pass']

    locals = {f'_type_{f.name}': f.type for f in fields}
    return dataclasses._create_fn('__init__',
                      [self_name] + [dataclasses._init_param(f) for f in fields if f.init] + ["**kwargs"],
                      body_lines,
                      locals=locals,
                      globals=globals,
                      return_type=None)

