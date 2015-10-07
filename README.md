# Stencil Validator [![Build Status](https://travis-ci.org/drewrwilson/stencilvalidator.svg)](https://travis-ci.org/drewrwilson/stencilvalidator)

A tool for checking whether a design is a valid stencil or not.

This is a work in progress. Alpha at best.

## Setup

For osx.

* Get homebrew!
* Install python! `brew install python`
* Give you homebrew the power of science! `brew tap homebrew/science`
* Install opencv `brew install opencv`

## Testing

`python test_stencil_validator.py`

There are a number of example stencils in the `test-stencils` directory.
The filename indicates whether or not the stencil is valid (eg `valid-black-lives-matter` vs `invalid-black-lives-matter`).
The invalid ones are just modified versions of the valid ones that include mistakes like shapes inside of shapes or letters that have sections without bridges. 

We currently have 6 tests that use these files as inputs. Tests are all located in the `tests` directory.
