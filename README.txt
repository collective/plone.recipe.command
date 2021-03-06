Introduction
============

The ``plone.recipe.command`` buildout recipe allows you to run a command
when a buildout part is installed or updated. It is very easy to use::

  [buildout]
  parts = command

  [command]
  recipe = plone.recipe.command
  command = cat README.txt

This configures a buildout part called ``command`` which lists the contents
of README.txt when it is installed.


Reference
=========

Unless otherwise specified all commands are run in the directory in which
buildout is invoked. Commands have to be present in the PATH or be specified
using an absolute pathname.

The following options are supported:

command
  Command to run when the buildout part is installed.

update-command
  Command to run when the buildout part is updated. This happens when
  buildout is run but the configuration for this buildout part has not
  changed.

location
  A list of filesystem paths that buildout should consider as being managed
  by this buildout part. These will be removed when buildout (re)installs
  or removes this part.

stop-on-error
  When ``yes``, ``on`` or ``true``, buildout will stop if the command ends
  with a non zero exit code.


Changes
=======

1.2 - Unreleased
----------------

* Added a test
  [regebro]


1.1 - 2010-02-25
----------------

* Added ``stop-on-error`` option to stop buildout on non zero return code of
  the command.
  [fschulze]

* Use subprocess instead of os.system.
  [fschulze]


1.0 - 2007-09-14
----------------

* Initial release.
