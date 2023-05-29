import React, { useEffect, useState } from "react";
import axios from "axios";

function Results() {
  let [resultList, setResultList] = useState([]);
  const [courses, setCourses] = useState([]);
  const [students, setStudents] = useState([]);

  // useEffect(() => {
  //   // Fetch courses from API
  //   axios
  //     .get("http://127.0.0.1:8000//allcourse/")
  //     .then((res) => {
  //       setCourses(res.data);
  //     })
  //     .catch((error) => {
  //       console.error(error);
  //     });

  //   // Fetch students from API
  //   axios
  //     .get("http://127.0.0.1:8000//alluser/")
  //     .then((res) => {
  //       setStudents(res.data);
  //     })
  //     .catch((error) => {
  //       console.error(error);
  //     });

  //   // Fetch results from API
    // axios
    //   .get("http://127.0.0.1:8000/allresult/")
    //   .then((res) => {
    //     const filteredResults = res.data.filter((result) => {
    //       // Filter based on courses and students
    //       return (
    //         courses.includes(result.shyft_resultcourse) &&
    //         students.includes(result.shyft_resultuser)
    //       );
    //     });
    //     setResultList(filteredResults);
    //   })
    //   .catch((error) => {
    //     console.error(error);
    //   });
  // }, [courses, students]);

  useEffect(() => {
    //console.log("check");
    axios
      .get("http://127.0.0.1:8000/allresult/")
      .then((res) => {
        // console.log("resultBeforeFilter",resultList)
        const filteredResults = res.data.filter((result) => {
          return (
            courses.some((course) => course.shyft_coursename === result.shyft_resultcourse)
            &&
            students.some((student) => (student.shyft_name) === result.shyft_resultuser)
            )
        });
        setResultList(filteredResults);
      });
    
  }, [courses, students]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000//alluser/")
      .then((res) => {
        console.log(res.data);
        setStudents(res.data);
      });
    
  }, []);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000//allcourse/")
      .then((res) => {
        // console.log(res.data);
        setCourses(res.data);
      });
    
  }, []);

  // console.log("result",resultList)
  // console.log("Student",students)
  // console.log("Courses",courses)

  const columns = [
    { Header: "Course Name", accessor: "shyft_resultcourse" },
    { Header: "Student Name", accessor: "shyft_resultuser" },
    { Header: "Score", accessor: "shyft_resultscore" },
  ];
  return (
    <>
    <div className="flex flex-col w-[1000px] justify-center items-center">
    <h1 className="text-2xl font-bold mb-10">Result List</h1>
      {resultList.length > 0 ? (
        <div className="flex flex-row justify center items center">
          <table className='border-2 border-slate-200'>
            <tr className='border-2 border-slate-200'>
              <th className="w-[100px] justify-center items-center">Course</th>
              <th className="w-[100px] justify-center items-center">Student</th>
              <th className="w-[100px] justify-center items-center">Score</th>
              {/* <th className="w-[50px] justify-center items-center">Action</th> */}
            </tr>
            <tbody>
              {resultList.map((row, index) => (
                
                <tr className={`${index % 2 === 0 ? 'bg-gray-100' : 'bg-white'}`}  key={index}>
                  <td className="w-[100px] justify-center items-center p-2">
                    {row.shyft_resultcourse}
                  </td>
                  <td className="w-[100px] justify-center items-center p-2">{row.shyft_resultuser}</td>
                  <td className="w-[100px] justify-center items-center p-2">{row.shyft_resultscore}</td>
                  {/* <td className="w-[50px] justify-center items-center p-2"
                    onClick={() => {
                      deleteResult(row);
                    }}
                  >
                    <button className="bg-red-500 rounded-full text-neutral-100 font-bold py-2 px-4 rounded-full">X</button>
                  </td> */}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      ) : null}
    </div>
  </>
  )
}

export default Results