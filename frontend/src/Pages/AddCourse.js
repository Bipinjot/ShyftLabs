import React from 'react'
import { Formik, Field, Form } from "formik";
import axios from "axios";

function AddCourse() {
  const addCourseHandler = async (values) => {
    let courseDetails = {
      coursename: values.courseName
    };
    console.log(courseDetails);
    try {
      const response = await fetch("http://127.0.0.1:8000/course/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(courseDetails), // Replace with your actual data
      });

      if (response.ok) {
        // Request was successful
        const data = await response.json();
        console.log(data); // Do something with the response data
        alert("Success");
        setTimeout(() => {
          window.location.reload();
        }, 1000);
      } else {
        // Request failed
        console.error("Error:", response.status);
      }
    } catch (error) {
      console.error("Error:", error);
    }
  };

  const validateField = (values) => {
    let error;
    if (!values) {
      error = "This is a required field";
    }
    return error;
  };

  return (
    <div className="flex w-[1000px] h-[700px] items-center justify-center">
      <Formik
        initialValues={{ courseName: ""}}
        onSubmit={addCourseHandler}
      >
        {({ errors, touched, isValidating }) => (
          <Form>
            <div className="flex flex-col gap-8">
              <h1 className="text-2xl font-bold">Add New Course</h1>
              <Field
                className="w-[500px] h-10 bg-none rounded-md outline-slate-50 border-slate-500 border-2 p-2"
                type="text"
                name="courseName"
                id="courseName"
                placeholder="Enter course name"
                validate={validateField}
              />
              {errors.courseName && touched.courseName && (
                <p className="text-red-700">{errors.courseName}</p>
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
  )
}

export default AddCourse