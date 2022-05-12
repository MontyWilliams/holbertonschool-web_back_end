const getListStudentIds = (anArray) => {
  if (!Array.isArray(anArray)) return [];

  return students.filter((item) => (item.location === city));
};

export default getListStudentIds;
