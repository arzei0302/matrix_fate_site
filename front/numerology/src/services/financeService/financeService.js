import api from "../axiosInstance"; 

const BASE_URL = "https://matrixaaa.duckdns.org";

const handleError = (error) => {
    console.error("Ошибка при получении данных:", error.message);
    throw error;
};

export const calculateNumerology = async ({ day, month, year }) => {
    try {
        const response = await api.post(`${BASE_URL}/finance/calculate-finance-matrix/`, {
            day,
            month,
            year,
           "category": "finance"
        });
        return response.data.matrix;
    } catch (error) {
        handleError(error);
    }
};

export const getBlocksMoney= async ({ j, c2, l }) => {

    
    try {
        const params = {
            block_j: j,
            task_c2: c2,
            task_l: l,
        };
        const response = await api.get(`${BASE_URL}/finance/blocks_money/5/tasks/`, { params });
        return response.data;
    } catch (error) {
        handleError(error);
    }
};

export const getDestinationSociety = async ({ t, u, v }) => {
    try {
        const params = {
            task_t: t ,
            task_u: u,
            task_v: v,
        };
        const response = await api.get(`${BASE_URL}/finance/destination_society/3/tasks/`, { params });
        return response.data;
    } catch (error) {
        handleError(error);
    }
};

export const getFincanceOpportunity= async ({a2 }) => {
    try {
        const params = {
            opportunity:a2,
        };
        const response = await api.get(`${BASE_URL}/finance/finance_opportunity/2/talents/`, { params });
        return response.data;
    } catch (error) {
        handleError(error);
    }
};

export const getKarmaTask=async({c,c1,c2})=>{
    try{
        const params={
            arcana_c:c,
            arcana_c1:c1,
            arcana_c2:c2
        };
        const response = await api.get(`${BASE_URL}/finance/karma_and_task_40/6/`, { params });
        return response.data;
    } catch (error) {
        handleError(error);
    }
    
}
// 
export const getTalents=async({a,b,c})=>{
    try{
        const params={
            birth_a:a,
            mature_c:c,
            youth_b:b
        };
        const response = await api.get(`${BASE_URL}/finance/talents/1/talents/`, { params });
        return response.data;
    } catch (error) {
        handleError(error);
    }
    
}


export const getWhatGivesMoney=async({l,j,c2})=>{
    try{
        const params={
            money_channel_l: l,
            money_j: j,
            realization_c2: c2
        };
        const response = await api.get(`${BASE_URL}/finance/what_gives_you_money/4/tasks/`, { params });
        return response.data;
    } catch (error) {
        handleError(error);
    }
    

}






