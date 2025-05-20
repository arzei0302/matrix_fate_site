import api from "../axiosInstance"; 

const BASE_URL = "https://numerology-calculator.fi/api";

const handleError = (error) => {
    console.error("Ошибка при получении данных:", error.message);
    throw error;
};
const catch403AndReturnData = (error) => {
    if (error.response?.status === 403 && error.response?.data?.category) {
        return {
            ...error.response.data,
            error: true,
            status: 403
        };
    }
    console.error("Ошибка:", error.message);
    throw error;
};

export const calculateCompabilityNumerology = async ({ day, month, year, day1, month1, year1 }) => {
    try {
        const [compatibilityResponse, matrixResponse] = await Promise.all([
            api.post(`https://numerology-calculator.fi/api/compatibility/calculate-compatibility/`, {
                day,
                month, 
                year,
                day2: day1,
                month2: month1,
                year2: year1,
                category:"compatibility"
            }),
            api.post(`https://numerology-calculator.fi/api/compatibility/calculate-matrix/`, {
                day,
                month,
                year,
                category:"compatibility"
            }),
            api.post(`https://numerology-calculator.fi/api/compatibility/calculate-matrix/`, {
                day:day1,
                month:month1,
                year:year1,
                category:"compatibility"
            })
        ]);

        return {
            compatibilityData: compatibilityResponse.data,
            matrixData: matrixResponse.data
        };
    } catch (error) {
        console.error("Ошибка запроса:", error);
        return null;
    }
}

export const getChildBusiness= async ({ c2,j,l }) => {

    
    try {
        const params = {
            arcana_c2: c2,
            arcana_j:j,
            arcana_l:l,
            category_id_or_title:"6"
        };
        const response = await api.get(`${BASE_URL}/compatibility/couple_money/6/couple_money/`, { params });
        return response.data.category;
    } catch (error) {
        return catch403AndReturnData(error);
    }
};

export const getChildDestiny= async ({ d2,j,k }) => {
    try {
        const params = {
            arcana_d2 : d2,
            arcana_j : j,
            arcana_k : k,
        };
        const response = await api.get(`${BASE_URL}/compatibility/couple_relations/7/couple_relations/`, { params });
        return response.data;
    } catch (error) {
        return catch403AndReturnData(error);
    }
};

export const getChildParentKarma = async ({b,c }) => {
    try {
        const params = {
            arcana_b : b,
            arcana_c : c,
        };
        const response = await api.get(`${BASE_URL}/compatibility/couple_resources/3/couple_resources/`, { params });
        return response.data;
    } catch (error) {
        return catch403AndReturnData(error);
    }
};

export const getChildPersonal=async({v})=>{
    try{
        const params={
            arcana_v:v,
        };
        const response = await api.get(`${BASE_URL}/compatibility/couples_task_for_society/5/couples_task_for_society/`, { params });
        return response.data;
    } catch (error) {
        return catch403AndReturnData(error);
    }
    
}
// 
export const getChildPoint=async({d,w,y})=>{
    try{
        const params={
            arcana_d : d,
            arcana_w : w,
            arcana_y : y
        };
        const response = await api.get(`${BASE_URL}/compatibility/tasks_for_couple/2/tasks_for_couple/`, { params });
        return response.data;
    } catch (error) {
        return catch403AndReturnData(error);
    }
    
}


export const getChildSelf=async({e})=>{
    try{
        const params={
            arcana_e: e,
        };
        const response = await api.get(`${BASE_URL}/compatibility/what_fills_the_vapor/4/what_fills_the_vapor/`, { params });
        return response.data;
    } catch (error) {
        return catch403AndReturnData(error);
    }
    

}

export const getTasksFromPast=async({a})=>{
    try{
        const params={
            arcana_a: a,
        };
        const response = await api.get(`${BASE_URL}/compatibility/why_did_you_meet/1/why_did_you_meet/`, { params });
        return response.data;
    } catch (error) {
        return catch403AndReturnData(error);
    }
    

}




