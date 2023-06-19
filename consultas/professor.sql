SELECT 
	C.NOME AS CURSO,
	TD.CODTURMA AS TURMA,
	CPA.resp_teacher_name,
	CPA.resp_quest_id as idpergunta,
	CPA.quest_description AS Pergunta,
	CPA.resp_ra,
	SUM(CASE WHEN CAST(CPA.resp_response AS VARCHAR) = '1' THEN 1 ELSE 0 END) AS INSUFICIENTE,
	SUM(CASE WHEN CAST(CPA.resp_response AS VARCHAR) = '2' THEN 1 ELSE 0 END) AS REGULAR,
	SUM(CASE WHEN CAST(CPA.resp_response AS VARCHAR) = '3' THEN 1 ELSE 0 END) AS BOM,
	SUM(CASE WHEN CAST(CPA.resp_response AS VARCHAR) = '4' THEN 1 ELSE 0 END) AS ÓTIMO,
	SUM(CASE WHEN CAST(CPA.resp_response AS VARCHAR) = '5' THEN 1 ELSE 0 END) AS EXCELENTE
FROM OPENQUERY (
	HOSTGATOR, 
	'SELECT * FROM sur_question LEFT JOIN sur_response_teacher ON(resp_quest_id = quest_id) WHERE periodo_id = 17 AND resp_quest_id <> 8' -- Alterar periodo_id segundo id em phpmyadmin
) CPA
INNER JOIN SMATRICULA MD ON(
	MD.RA = CAST(CPA.resp_ra AS VARCHAR) COLLATE SQL_Latin1_General_CP1_CI_AI
)
INNER JOIN STURMADISC TD ON (	
	TD.CODCOLIGADA = MD.CODCOLIGADA
	AND TD.IDTURMADISC = MD.IDTURMADISC
	AND TD.IDPERLET = MD.IDPERLET
)
INNER JOIN SHABILITACAOFILIAL HF ON(
	HF.CODCOLIGADA = TD.CODCOLIGADA
	AND HF.IDHABILITACAOFILIAL = TD.IDHABILITACAOFILIAL
)
INNER JOIN SCURSO C ON(
	C.CODCOLIGADA = HF.CODCOLIGADA
	AND C.CODCURSO = HF.CODCURSO
)
WHERE MD.IDPERLET = 79 -- Período letivo atual
GROUP BY
	C.NOME	
	, TD.CODTURMA
	, CPA.resp_teacher_name
	, CPA.resp_quest_id
	, CPA.quest_description
	, CPA.resp_ra
ORDER BY 
	C.NOME	
	, TD.CODTURMA
	, CPA.resp_teacher_name
	, CPA.resp_quest_id
	, CPA.quest_description
	, CPA.resp_ra