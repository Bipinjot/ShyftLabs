import React, { useState, useEffect } from "react";
import { Formik, Form, Field, ErrorMessage } from "formik";

const MyComponent = () => {
  const [options1, setOptions1] = useState([]);
  const [options2, setOptions2] = useState([]);

  // Function to fetch options for dropdown 1
  const fetchOptions1 = () => {
    fetch("http://127.0.0.1:8000//alluser/")
      .then((response) => response.json())
      .then((data) => {
        setOptions1(data);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  // Function to fetch options for dropdown 2
  const fetchOptions2 = () => {
    fetch("http://127.0.0.1:8000//allcourse/")
      .then((response) => response.json())
      .then((data) => {
        setOptions2(data);
      })
      .catch((error) => {
        console.error(error);
      });
  };
  // console.log(options1);
  // console.log(options2);
  // Call fetchOptions1 and fetchOptions2 when the component mounts
  useEffect(() => {
    fetchOptions1();
    fetchOptions2();
  }, []);

  // Function to handle form submission
  // Function to handle form submission
const handleSubmit = (values, { setSubmitting }) => {
  // Perform validation
  if (!values.dropdown1 || !values.dropdown2 || !values.score) {
    alert('Please select options for all dropdowns.'); // You can use other form validation techniques as well
    setSubmitting(false);
    return;
  }

  // Prepare the data for the POST request
  const data = {
    username: values.dropdown1, // Use the key instead of value
    coursename: values.dropdown2, // Use the key instead of value
    score: values.score
  };
  console.log(data);

  // Send the POST request
  fetch('http://127.0.0.1:8000/result/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
    .then(response => response.json())
    .then(result => {
      // Handle the API response
      console.log(result);
      alert("Success");
        setTimeout(() => {
          window.location.reload();
        }, 1000);
    })
    .catch(error => {
      console.error(error);
    })
    .finally(() => {
      setSubmitting(false);
    });
};

  return (
    <div className="flex w-[1000px] h-[700px] items-center justify-center">
      <Formik
        initialValues={{ dropdown1: "", dropdown2: "" }}
        onSubmit={handleSubmit}
      >
        <Form className="flex flex-col items-center p-4">
        <div className="flex flex-col gap-8">
              <h1 className="text-2xl font-bold">Add New Student</h1>
          <div className="flex flex-col">
            <label htmlFor="dropdown1" className="mb-2">
              Student Name
            </label>
            <Field
              as="select"
              id="dropdown1"
              name="dropdown1"
              required
              className="w-[500px] h-10 bg-none rounded-md outline-slate-50 border-slate-500 border-2 p-2"
            >
              <option value="">Select...</option>
              {options1.map((option) => (
                <option key={option.shyft_userid} value={option.shyft_name}>
                  {option.shyft_name}
                </option>
              ))}
            </Field>
            <ErrorMessage
              name="dropdown1"
              component="div"
              className="text-red-500"
            />
          </div>
          <div className="flex flex-col">
            <label htmlFor="dropdown2" className="mb-2">
              Course Name
            </label>
            <Field
              as="select"
              id="dropdown2"
              name="dropdown2"
              required
              className="w-[500px] h-10 bg-none rounded-md outline-slate-50 border-slate-500 border-2 p-2"
            >
              <option value="">Select...</option>
              {options2.map((option) => (
                <option key={option.shyft_courseid} value={option.shyft_coursename}>
                  {option.shyft_coursename}
                </option>
              ))}
            </Field>
            <ErrorMessage
              name="dropdown2"
              component="div"
              className="text-red-500"
            />
          </div>
          <div className="flex flex-col">
            <label htmlFor="score" className="mb-2">
              Score
            </label>
            <Field
              as="select"
              id="score"
              name="score"
              required
              className="w-[500px] h-10 bg-none rounded-md outline-slate-50 border-slate-500 border-2 p-2"
            >
              <option value="">Select...</option>
              <option value="A">A</option>
              <option value="B">B</option>
              <option value="C">C</option>
              <option value="D">D</option>
              <option value="E">E</option>
            </Field>
            <ErrorMessage
              name="score"
              component="div"
              className="text-red-500"
            />
          </div>
          <button
            type="submit"
            className="flex p-4 justify-center items-center bg-green-600 shadow-md rounded-md uppercase font-bold text-2xl text-neutral-100 mt-20"
          >
            Add
          </button>
          </div>
        </Form>
      </Formik>
    </div>
  );
};

export default MyComponent;
