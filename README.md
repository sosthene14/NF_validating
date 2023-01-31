<<<<<<< HEAD
NF Validator
A simple and easy to use package for validating names and surnames written in Unicode.
-
Installation
-
You can install the nf_validator package using pip. To do so, open a terminal and run:


    pip install nf_validator


Usage
-
Here is an example of how to use the nf_validating function from the nf_validator package:


    import nf_validator

    name = "Jürgen Müller"

    valid_name = nf_validator.nf_validating(name)

    if valid_name:

        print("Name is valid:", valid_name)

    else:

        print("Name is not valid")


In this example, the nf_validating function takes a string as an argument, splits it into a list of words, and then joins the words back into a single string. The resulting string is then normalized using the NFKD normalization form and encoded into ASCII, while ignoring any invalid characters. The final step is to check if the resulting string consists only of alphabetic characters. If so, the name is considered valid and the original, non-normalized string is returned. If not, the function returns False.

Contributing
If you would like to contribute to this package, please feel free to submit a pull request. All contributions are welcome!

License
This project is licensed under the MIT License. See the LICENSE file for details.
=======
# NF_validating
A simple Name Validation package, you can easily verify the validity of names in just a few lines of code

