import axios from "axios";
import React, { useEffect, useState } from "react";
import ReactTable from "react-table";

function StudentList() {
  const deleteStudent = async (row) => {
    console.log(row)
    await axios
      .delete(
        `https://shyftappbackend--q3xeitu.ambitiousisland-adc17e0d.westus2.azurecontainerapps.io/deleteuser/${row.id}`
      )
      .then((res) => {
        alert("Deleted");
      })
      .catch((err) => {
        console.log("Error in delete");
      });
  };
  let [studentList, setStudentList] = useState([]);
  useEffect(() => {
    console.log("check");
    axios
      .get("https://6471219d3de51400f7255809.mockapi.io/test/students")
      .then((res) => {
        console.log(res.data);
        setStudentList(res.data);
      });
  }, []);
  const columns = [
    {
      Header: "Full Name",
      accessor: (row) => `${row.shyft_name} ${row.shyft_familyname}`,
    },
    { Header: "DOB", accessor: "shyft_dob" },
    { Header: "Email", accessor: "shyft_email" },
  ];
  return (
    <>
      <div className="flex flex-col w-[1000px] justify-center items-center">
      <h1 className="text-2xl font-bold mb-10">Student List</h1>
        {studentList.length > 0 ? (
          <div className="flex flex-row justify center items center">
            <table className='border-2 border-slate-200'>
              <tr className='border-2 border-slate-200'>
                <th className="w-[400px] justify-center items-center">Full Name</th>
                <th className="w-[100px] justify-center items-center">DOB</th>
                <th className="w-[200px] justify-center items-center">Email</th>
                <th className="w-[50px] justify-center items-center">Action</th>
              </tr>
              <tbody>
                {studentList.map((row, index) => (
                  
                  <tr className={`${index % 2 === 0 ? 'bg-gray-100' : 'bg-white'}`}  key={index}>
                    <td className="w-[400px] justify-center items-center p-2">
                      {row.shyft_name} {row.shyft_familyname}
                    </td>
                    <td className="w-[200px] justify-center items-center p-2">{row.shyft_dob}</td>
                    <td className="w-[200px] justify-center items-center p-2">{row.shyft_email}</td>
                    <td className="w-[50px] justify-center items-center p-2"
                      onClick={() => {
                        deleteStudent(row);
                      }}
                    >
                      <button className="bg-red-500 rounded-full text-neutral-100 font-bold py-2 px-4 rounded-full">X</button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ) : null}
      </div>
    </>
  );
}
export default StudentList;
