import React from "react";
import { Formik, Field, Form } from "formik";
import axios from "axios";

function AddStudent() {
  const addStudentHandler = async (values) => {
    let studentDetails = {
      shyft_name: values.firstName,
      shyft_familyname: values.familyName,
      shyft_dob: values.dob,
      shyft_email: values.email,
    };
    console.log(studentDetails);
    await axios
      .post(
        "https://shyftappbackend--q3xeitu.ambitiousisland-adc17e0d.westus2.azurecontainerapps.io/user",
        { studentDetails: studentDetails }
      )
      .then((res) => {
        alert("Success");
        setTimeout(() => {
          window.location.reload();
        }, 1000);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  const validateField = (values) => {
    let error;
    if (!values) {
      error = "This is a required field";
    }
    return error;
  };

  const validateEmail = (value) => {
    let error;
    if (!value) {
      error = "This is a required field";
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)) {
      error = "Invalid email id";
    }
    return error;
  };
  return (
    <div className="flex w-[1000px] h-[700px] items-center justify-center">
      <Formik
        initialValues={{ firstName: "", familyName: "", dob: "", email: "" }}
        onSubmit={addStudentHandler}
      >
        {({ errors, touched, isValidating }) => (
          <Form>
            <div className="flex flex-col gap-8">
              <h1 className="text-2xl font-bold">Add New Student</h1>
              <Field
                className="w-[500px] h-10 bg-none rounded-md outline-slate-50 border-slate-500 border-2 p-2"
                type="text"
                name="firstName"
                id="firstName"
                placeholder="Enter first name"
                validate={validateField}
              />
              {errors.firstName && touched.firstName && (
                <p className="text-red-700">{errors.firstName}</p>
              )}

              <Field
                className="w-[500px] h-10 bg-none rounded-md outline-slate-50 border-slate-500 border-2 p-2"
                type="text"
                name="familyName"
                id="familyName"
                placeholder="Enter family name"
                validate={validateField}
              />
              {errors.familyName && touched.familyName && (
                <p className="text-red-700">{errors.familyName}</p>
              )}

              <div className="flex flex-col">
                <p className="text-lg">Select DOB</p>
                <Field
                  className="w-[500px] h-10 bg-none rounded-md outline-slate-50 border-slate-500 border-2 p-2"
                  type="date"
                  name="dob"
                  id="dob"
                  placeholder="Select DOB"
                  validate={validateField}
                />
                {errors.dob && touched.dob && (
                  <p className="text-red-700">{errors.dob}</p>
                )}
              </div>

              <Field
                className="w-[500px] h-10 bg-none rounded-md outline-slate-50 border-slate-500 border-2 p-2"
                type="email"
                name="email"
                id="email"
                placeholder="Enter email"
                validate={validateEmail}
              />
              {errors.email && touched.email && (
                <p className="text-red-700">{errors.email}</p>
              )}

              <button
                type="submit"
                className="flex p-4 justify-center items-center bg-green-600 shadow-md rounded-md uppercase font-bold text-2xl text-neutral-100 mt-20"
              >
                Add
              </button>
            </div>
          </Form>
        )}
      </Formik>
    </div>
  );
}

export default AddStudent;
