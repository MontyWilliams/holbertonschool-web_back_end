const getListStudentIds = (Array) => {
  if (!Array.isArray(Array)) return [];

  return Array.map((object) => object.id);
};

export default getListStudentIds;
