import api from "../axiosInstance"; 

const BASE_URL = "https://matrixaaa.duckdns.org";

const handleError = (error) => {
    console.error("Ошибка при получении данных:", error.message);
    throw error;
};

   
export const calculateNumerology = async ({ day, month, year }) => {
    try {
        const response = await api.post(`${BASE_URL}/child/calculate-child-matrix/`, {
            day,
            month,
            year,
            category:"child"
        });
        return response.data.matrix;
    } catch (error) {
        handleError(error);
    }
};

export const getChildBusiness= async ({ a }) => {

    
    try {
        const params = {
            arcana_a: a,
        };
        const response = await api.get(`${BASE_URL}/child/child_business_card/1/`, { params });
        return response.data;
    } catch (error) {
        handleError(error);
    }
};

export const getChildDestiny= async ({ r,s,y }) => {
    try {
        const params = {
            arcana_r: r,
            arcana_s: s,
            arcana_y: y,
        };
        const response = await api.get(`${BASE_URL}/child/child_destiny/6/`, { params });
        return response.data;
    } catch (error) {
        handleError(error);
    }
};

export const getChildParentKarma = async ({a2,a,a1 }) => {
    try {
        const params = {
            arcana_a: a,
            arcana_a1: a1,
            arcana_a2: a2,
        };
        const response = await api.get(`${BASE_URL}/child/child_parent_karma/7/`, { params });
        return response.data;
    } catch (error) {
        handleError(error);
    }
};

export const getChildPersonal=async({b,c})=>{
    try{
        const params={
            arcana_b:b,
            arcana_c:c,
        };
        const response = await api.get(`${BASE_URL}/child/child_personal_qualities/2/`, { params });
        return response.data;
    } catch (error) {
        handleError(error);
    }
    
}
// 
export const getChildPoint=async({e})=>{
    try{
        const params={
            arcana_e: e,
        };
        const response = await api.get(`${BASE_URL}/child/child_point_of_comfort/4/`, { params });
        return response.data;
    } catch (error) {
        handleError(error);
    }
    
}


export const getChildSelf=async({a2})=>{
    try{
        const params={
            arcana_a2: a2,
        };
        const response = await api.get(`${BASE_URL}/child/child_self_realization/3/`, { params });
        return response.data;
    } catch (error) {
        handleError(error);
    }
    

}

export const getTasksFromPast=async({d,d1,d2})=>{
    try{
        const params={
            arcana_d: d,
            arcana_d1: d1,
            arcana_d2: d2,
        };
        const response = await api.get(`${BASE_URL}/child/tasks_from_past_lives/5/`, { params });
        return response.data;
    } catch (error) {
        handleError(error);
    }
    

}




